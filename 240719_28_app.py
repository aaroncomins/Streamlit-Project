# In the terminal use:
# python3 -m memory_profiler app.py

# Mem Package
from memory_profiler import profile 

# Add "@profile" one row above the Main function

# To plot it, go to your terminal and run:
# mprof run app.py

# After it creates the mprof, go to your terminal and run:
# mprof plot

# Save the plot if desired and then run:
# mprof plot --flame