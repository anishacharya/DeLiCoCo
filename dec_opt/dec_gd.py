import numpy as np
import time

INIT_WEIGHT_STD = 0.01
LOSS_PER_EPOCH = 10
np.random.seed(1)


class DecGD:
    def __init__(self, feature, target, hyper_param, model):
        self.A = feature
        self.y = target
        self.param = hyper_param
        self.model = model

        # initialize x_hat, x_estimate  Ax = y is the problem we are solving
        # -------------------------------------------------------------------
        self.losses = np.zeros(self.param.epochs + 1)
        self.num_samples, self.num_features = self.A.shape

        self.model.x = np.random.normal(0, INIT_WEIGHT_STD, size=(self.num_features,))
        self.model.x = np.tile(self.model.x, (self.param.n_cores, 1)).T

        self.model.x_estimate = np.copy(self.model.x)
        self.x_hat = np.copy(self.model.x)

        # Now Distribute the Data among machines
        # ----------------------------------------
        self.data_partition_ix, self.num_samples_per_machine = self._distribute_data()

        # Decentralized Training
        # --------------------------
        self._train()

    def _distribute_data(self):
        data_partition_ix = []
        num_samples_per_machine = self.num_samples // self.param.n_cores
        all_indexes = np.arange(self.num_samples)
        np.random.shuffle(all_indexes)

        for machine in range(0, self.param.n_cores - 1):
            data_partition_ix += [
                all_indexes[num_samples_per_machine * machine: num_samples_per_machine * (machine + 1)]]
        # put the rest in the last machine
        data_partition_ix += [all_indexes[num_samples_per_machine * (self.param.n_cores - 1):]]
        print("All but last machine has {} data points".format(num_samples_per_machine))
        print("length of last machine indices:", len(data_partition_ix[-1]))
        return data_partition_ix, num_samples_per_machine

    def _train(self):
        compute_loss_every = int(self.num_samples_per_machine / LOSS_PER_EPOCH) + 1
        all_losses = np.zeros(int(self.num_samples_per_machine * self.param.epochs / compute_loss_every) + 1)
        train_start = time.time()
        for epoch in np.arange(self.param.epochs):
            for iteration in range(self.num_samples_per_machine):
                t = epoch * self.num_samples_per_machine + iteration
                if t % compute_loss_every == 0:
                    loss = self.model.loss(self.A, self.y)
                    print('t {} epoch {} iter {} loss {} elapsed {}s'.format(t, epoch, iteration, loss,
                                                                             time.time() - train_start))
                    all_losses[t // compute_loss_every] = loss
                    if np.isinf(loss) or np.isnan(loss):
                        print("training exit - diverging")
                        break
                lr = self.model.lr(epoch=epoch, iteration=iteration, num_samples=self.num_samples_per_machine,
                                   tau=self.num_features)
                # Gradient step
                x_plus = np.zeros_like(self.x)
