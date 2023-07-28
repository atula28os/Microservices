"""_Generate CLI Command_
Fire: Using Fire we can create any function/module/object into CLI
"""
import fire
from mylib.logic import wiki, summary

if __name__ == '__main__':
    fire.Fire(wiki)
    fire.Fire(summary)
    