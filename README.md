# GraphWeaver ![](https://img.shields.io/badge/License-MIT-blue)

A Tool for constructing method call chain and calculate suspicion in system

# Why this Name

Just a temp name. I am battling a spider-like monster in cyberspace recently.
So the Weaver may be a good alternative for spider.
Also, we firstly want to use ApsectJ which has a phase called weave.
It sounds cool. 

# Introduction

| Name   | Description                   |
|--------|-------------------------------|
| result | Store the results(e.g. graph) |
| utils  | Collect some tools for use    |

# How to Use

We use python 3.9.
- Clone the project.
  - `git clone https://github.com/MartyLinZY/GraphWeaver.git`
- Install the required packages.
  - `cd GrapWeaver`
  - `pip install -r requirement.txt`
- Get the system log(e.g. Cassandra) and put under the project path
- Run the `log2json.py`
- Run the `main.py`