'''
Calculates the next time step for the state of the nodes
'''
import numpy as np


'''
The attribute state in every node defines the last state of the node. At the dictionary activityTimeLine we have the
evolution of the values for the state over time.
'''
def edges_update(graph, t, function='hebbian', delta = 0.2, speed_factor = 0.3, thres_h = 0.1, persistence=None, amplification=None):
    if t % 5 == 0:
        print 'Time: ', t

    g = graph.copy()

    for edge in g.edges():
        source_node, target_node = edge
        old_weight = g.get_edge_data(source_node,target_node).values()[0]['weight']
        source = g.node[source_node]['state']
        target = g.node[target_node]['state']

        if function == 'hebbian':
            if persistence == None:
                print 'Error! Give persistence value to calculate hebbian operations!'
                exit(0)
            else:
                variation = speed_factor * (source * target * (1 - target) + persistence * target)

        elif function == 'slhom':
            if amplification == None:
                print 'Error! Amplification not set!'
                exit(0)
            else:
                variation = old_weight+ amplification * old_weight * (1 - old_weight) * (thres_h - np.abs(source - target))

        elif function == 'advanced_linear':
            if amplification == None:
                print 'Error! Amplification not set!'
                exit(0)

            variation = (old_weight + amplification * ((1 - old_weight) * (np.abs(thres_h - np.abs(source - target))+(
                thres_h - np.abs(source - target))) / 2 + old_weight * (np.abs(thres_h- np.abs(source - target))-(
                thres_h - np.abs(source - target))) / 2))

        elif function == 'simple_quadratic':
            if amplification == None:
                print 'Error! Amplification not set!'
                exit(0)

            variation = (old_weight + amplification * old_weight * (1 - old_weight) * (thres_h^ 2 - np.abs(source - target) ^ 2))

        elif function == 'advanced_quadratic':
            if amplification == None:
                print 'Error! Amplification not set!'
                exit(0)

            variation = (old_weight + amplification * ((1 - old_weight) * (np.abs(thres_h^2 - np.abs(source - target)^2) + (
            thres_h ^ 2 - np.abs(source - target) ^ 2)) / 2 + old_weight * (np.abs(thres_h ^ 2 - np.abs(source - target) ^ 2) - (
                                                           thres_h ^ 2 - np.abs(source - target) ^ 2)) / 2))

        else:
            print '[Edges] Your combinational function doesn\'t exist'
            exit(0)

        new_weight = old_weight + speed_factor * (variation - old_weight )*delta # homophily model

        #new_weight = new_weight if new_weight >= 0 else 0
        #new_weight = new_weight if new_weight <= 1 else 1

        try:
            g[source_node][target_node][0]['weightTimeLine'].update({t:new_weight})
        except:
            print t, source, target, g[source][target]['weightTimeLine']


        try:
            g[source_node][target_node][0]['weight'] = np.asscalar(new_weight)
        except:
            g[source_node][target_node][0]['weight'] = new_weight

    return g