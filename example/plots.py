from dec_opt.utils import unpickle_dir
import numpy as np
import matplotlib.pyplot as plt


def plot_results(repeats, label, plot='train'):
    scores = []
    for result in repeats:
        loss_val = result[0] if plot == 'train' else result[1]
        scores += [np.log(loss_val)]

    # scores = np.array(scores)
    # scores[scores == 0] = 1e20
    # scores[np.isinf(scores)] = 1e20
    # scores[np.isnan(scores)] = 1e20

    mean = np.mean(scores, axis=0)
    x = np.arange(mean.shape[0])
    UB = mean + np.std(scores, axis=0)
    LB = mean - np.std(scores, axis=0)

    plt.plot(x, mean, label=label)
    plt.fill_between(x, LB, UB, alpha=0.2)


if __name__ == '__main__':
    # Example plot generation :
    # Follow this template to generate your own combination of plots
    # remember the naming convention of the results
    # Load all results of a particular data-set
    data = unpickle_dir(d='./results/mnist')
    baselines = unpickle_dir(d='./results/baselines')
    print('Loaded Data')

    # Now Lets
    plt.figure()
    fig = plt.gcf()

    # Specify what result runs you want to plot together

    """ 
    Understand Effects of Varying Q
    """
    # Varying Q under different consensus LR, while keeping topology and Compression same ##
    # Consensus LR = 0.01
    # plt.title('Effect of Varying Q when Consensus LR = 0.01')
    # plot_results(repeats=data['ours.9.ring.0.0.01.top'], label='Q=0, CLR=0.01')
    # plot_results(repeats=data['ours.9.ring.1.0.01.top'], label='Q=1, CLR=0.01')
    # plot_results(repeats=data['ours.9.ring.2.0.01.top'], label='Q=2, CLR=0.01')
    # plot_results(repeats=data['ours.9.ring.3.0.01.top'], label='Q=3, CLR=0.01')
    # plot_results(repeats=data['ours.9.ring.4.0.01.top'], label='Q=4, CLR=0.01')

    # Consensus LR = 0.05
    # plt.title('Effect of Varying Q when Consensus LR = 0.05')
    # plot_results(repeats=data['ours.9.ring.0.0.05.top'], label='Q=0, CLR=0.05')
    # plot_results(repeats=data['ours.9.ring.1.0.05.top'], label='Q=1, CLR=0.05')
    # plot_results(repeats=data['ours.9.ring.2.0.05.top'], label='Q=2, CLR=0.05')
    # plot_results(repeats=data['ours.9.ring.3.0.05.top'], label='Q=3, CLR=0.05')
    # plot_results(repeats=data['ours.9.ring.4.0.05.top'], label='Q=4, CLR=0.05')

    # Consensus LR = 0.1
    # plt.title('Effect of Varying Q when Consensus LR = 0.1')
    # plot_results(repeats=data['ours.9.ring.0.0.1.top'], label='Q=0, CLR=0.1')
    # plot_results(repeats=data['ours.9.ring.1.0.1.top'], label='Q=1, CLR=0.1')
    # plot_results(repeats=data['ours.9.ring.2.0.1.top'], label='Q=2, CLR=0.1')
    # plot_results(repeats=data['ours.9.ring.3.0.1.top'], label='Q=3, CLR=0.1')
    # plot_results(repeats=data['ours.9.ring.4.0.1.top'], label='Q=4, CLR=0.1')
    #
    # # Consensus LR = 0.3
    # plt.title('Effect of Varying Q and Consensus')
    # plot_results(repeats=data['ours.9.ring.0.0.3.top'], label='Q=0, CLR=0.3')
    # plot_results(repeats=data['ours.9.ring.1.0.3.top'], label='Q=1, CLR=0.3')
    # plot_results(repeats=data['ours.9.ring.2.0.3.top'], label='Q=2, CLR=0.3')
    # plot_results(repeats=data['ours.9.ring.3.0.3.top'], label='Q=3, CLR=0.3')
    # plot_results(repeats=data['ours.9.ring.4.0.3.top'], label='Q=4, CLR=0.3')

    # Consensus LR = 0.5
    # plt.title('Effect of Varying Q with Consensus LR = 0.5')
    # plot_results(repeats=data['ours.9.ring.0.0.5.top'], label='Q=0, CLR=0.5')
    # plot_results(repeats=data['ours.9.ring.1.0.5.top'], label='Q=1, CLR=0.5')
    # plot_results(repeats=data['ours.9.ring.2.0.5.top'], label='Q=2, CLR=0.5')
    # plot_results(repeats=data['ours.9.ring.3.0.5.top'], label='Q=3, CLR=0.5')
    # plot_results(repeats=data['ours.9.ring.4.0.5.top'], label='Q=4, CLR=0.5')

    # Consensus LR = 0.7
    # plt.title('Effect of Varying Q with Consensus LR = 0.5')
    # plot_results(repeats=data['ours.9.ring.0.0.7.top'], label='Q=0, CLR=0.7')
    # plot_results(repeats=data['ours.9.ring.1.0.7.top'], label='Q=1, CLR=0.7')
    # plot_results(repeats=data['ours.9.ring.2.0.7.top'], label='Q=2, CLR=0.7')
    # plot_results(repeats=data['ours.9.ring.3.0.7.top'], label='Q=3, CLR=0.7')
    # plot_results(repeats=data['ours.9.ring.4.0.7.top'], label='Q=4, CLR=0.7')

    # Consensus LR = 1
    # plt.title('Effect of Varying Q with Consensus LR = 1')
    # plot_results(repeats=data['ours.9.ring.0.1.top'], label='Q=0, CLR=1')
    # plot_results(repeats=data['ours.9.ring.1.1.top'], label='Q=1, CLR=1')
    # plot_results(repeats=data['ours.9.ring.2.1.top'], label='Q=2, CLR=1')
    # plot_results(repeats=data['ours.9.ring.3.1.top'], label='Q=3, CLR=1')
    # plot_results(repeats=data['ours.9.ring.4.1.top'], label='Q=4, CLR=1')

    plt.xlabel('epochs')
    plt.ylabel('loss (log)')
    plt.grid(axis='both')
    plt.legend()
    plt.show()