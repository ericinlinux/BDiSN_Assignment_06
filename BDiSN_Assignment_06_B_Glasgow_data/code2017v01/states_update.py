

'''
Calculates the next time step for the state of the nodes
'''
import numpy as np


'''
The attribute state in every node defines the last state of the node. At the dictionary activityTimeLine we have the
evolution of the values for the state over time.
'''
def states_update(g, t, combination_function='sum', speed_factor = 0.3, delta = 1, scaling_factor=None, normalizing_factor=None,
                  steepness=None, threshold=None):
    combination_functions_list = ['id', 'sum', 'ssum', 'norsum', 'adnorsum', 'slogistic', 'alogistic', 'adalogistic']

    g_new = g.copy()

    # Updating the state of each node in the graph
    for node in g.nodes():
        aggimpact = 0
        sum_weights = 0
        # Calculate the agregated impact from the neighbours, together with the sum of the weights.
        for neigh in g.neighbors(node):
            #connect = g.get_edge_data(neigh, node)['weight']
            connect = g[neigh][node][0]['weightTimeLine'][t-1]
            #connect = g.get_edge_data(neigh, node).values()[0]['weight']
            sum_weights = sum_weights + connect
            try:
                aggimpact = aggimpact + g.node[neigh]['activityTimeLine'][t-1]*connect
            except:
                print t, neigh
                exit(0)

        # Defining aggimpact ['id', 'sum', 'ssum', 'norsum', 'adnorsum', 'slogistic', 'alogistic', 'adalogistic']
        if combination_function == 'id' or combination_function == 'sum':
            aggimpact = aggimpact
        elif combination_function == 'ssum':
            # Use scaling_factor
            if scaling_factor == None:
                print 'Error! Give scaling factor as an input to this function!'
            else:
                try:
                    scaling_f = scaling_factor[node]
                    aggimpact = aggimpact/scaling_f
                except:
                    print 'Scaling factor has to be a dictionary!'
                    print scaling_factor
                    exit(0)

        elif combination_function == 'norsum':
            # Use normalization_factor
            if normalizing_factor == None:
                print 'Error! Give normalization factor as an input to this function!'
            else:
                try:
                    normalizing_f = normalizing_factor[node]
                    aggimpact = aggimpact / normalizing_f
                except:
                    print 'Normalization factor has to be a dictionary!'
                    print normalizing_factor
                    exit(0)

        elif combination_function == 'adnorsum':
            aggimpact = aggimpact / sum_weights

        elif combination_function == 'slogistic':
            if steepness == None or threshold == None:
                print 'Steepness and threshold should be passed to the function for slogistic!'
                exit(0)
            try:
                steep = steepness[node]
                thres = threshold[node]
            except:
                print 'Dictionary is not built with the right keys!'
                exit(0)
            aggimpact = 1 / (1 + np.exp(-steep * (aggimpact - thres)))

        elif combination_function == 'alogistic':
            if steepness == None or threshold == None:
                print 'Steepness and threshold should be passed to the function for alogistic!'
                exit(0)
            try:
                steep = steepness[node]
                thres = threshold[node]
            except:
                print 'Dictionary is not built with the right keys (alogistic)!'
                exit(0)
            aggimpact = ((1 / (1 + np.exp(-steep * (aggimpact - thres)))) - (1 / (1 + np.exp(steep * thres)))) * (1 + np.exp(-steep * thres))

        elif combination_function == 'adalogistic':
            if steepness == None or threshold == None:
                print 'Steepness and threshold should be passed to the function for adalogistic!'
                exit(0)
            try:
                steep = steepness[node]
                thres = threshold[node]
            except:
                print 'Dictionary is not built with the right keys (adalogistic)!'
                exit(0)
            aggimpact = ((1 / (1 + np.exp(-steep * (aggimpact - thres * sum_weights)))) - (1 / (1 + np.exp(steep * thres)))) * (1 + np.exp(-steep * thres))
        else:
            print 'Your combination function is not in the possible list of functions:', combination_functions_list
            exit(0)

        if aggimpact > 0:
            # new_state = store_states(i, step-1) + update_s * (aggimpact - store_states(i, step-1)); %calculate the new state value
            old_activity = g.node[node]['state']
            new_activity = old_activity + speed_factor * (aggimpact - old_activity) * delta
            try:
                new_activity = np.asscalar(new_activity)
            except:
                new_activity=new_activity

            g_new.node[node]['activityTimeLine'].update({t: new_activity})
            g_new.node[node]['state'] = new_activity
        else:
            try:
                actual_state = np.asscalar(g.node[node]['state'])
            except:
                actual_state = g.node[node]['state']
            g_new.node[node]['activityTimeLine'].update({t: actual_state})
    return g_new
