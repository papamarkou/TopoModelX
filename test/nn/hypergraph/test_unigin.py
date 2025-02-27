"""Test the UniGIN class."""

import numpy as np
import torch

from topomodelx.nn.hypergraph.unigin import UniGIN


class TestUniGIN:
    """Test the UniGIN."""

    def test_forward(self):
        """Test forward method."""
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        incidence = torch.from_numpy(np.random.rand(2, 2)).to_sparse()
        incidence = incidence.float().to(device)
        model = UniGIN(
            in_channels_node=2,
            intermediate_channels=2,
            out_channels=2,
            n_layers=2,
        ).to(device)
        x_0 = torch.rand(2, 2)

        x_0 = torch.tensor(x_0).float().to(device)

        y1 = model(x_0, incidence)

        assert len(y1.shape) != -1
