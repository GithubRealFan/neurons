import torch
import bittensor
import subprocess

class Bito(torch.nn.Module):
    def __init__(self):
        super(Bito, self).__init__()

    def forward(self, text="hey"):
        command = ['bito']
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(text.encode())
        output = stdout.decode().strip()
        return output

neuron = bittensor.neuron.Neuron(Bito())

neuron.run()