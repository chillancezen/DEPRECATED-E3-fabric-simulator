# E3-fabric-simulator
:bowtie:E3-net fabric topology simulator orchestrated in Linux env

 -  edit the sample.yaml to define your network topology,note that some parameters are optional,please refer to the sample 
 -  use `#./orchestrate.py generate` to produce the script to generate the network.
 -  use `#./orchestrate.py degenerate` to produce the script to degenerate the network.
 -  usually you do not need to call them, use Makefile (which is smart enough to handle the dependency among them) instead
 -  `#make` generates the scripts
 -  `#make clean` removes the scripts
 -  `#make install` will prepare the defined environment
 -  `#make uninstall` will uninstall the environment eventually
 
 
