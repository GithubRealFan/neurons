import torch
import openai
import argparse
import bittensor
import subprocess

from typing import List, Dict


class Bito( bittensor.BasePromptingMiner ):
    @classmethod
    def check_config( cls, config: 'bittensor.Config' ): pass

    def backward( self, messages: List[Dict[str, str]], response: str, rewards: torch.FloatTensor ) -> str: pass

    @classmethod
    def add_args( cls, parser: argparse.ArgumentParser ): pass

    def __init__( self ):
        super( Bito, self ).__init__()

    def forward( self, messages: List[Dict[str, str]]  ) -> str:
        command = ['bito']
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate(messages.encode())
        output = stdout.decode().strip()
        return output

if __name__ == "__main__":
    bittensor.utils.version_checking()
    Bito().run()