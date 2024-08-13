# This is code you put into an py file that you have made already

# In the terminal use:
# python3 -m memory_profiler app.py

# Mem Package
from memory_profiler import profile 

# Add "@profile" one row above the Main function (def)

# To plot it, go to your terminal and run:
# mprof run app.py (app28_memory_profiling_st.apps.py)

# After it creates the mprof, go to your terminal and run:
# mprof plot

# Save the plot if desired and then run:
# mprof plot --flame