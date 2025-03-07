import os
import tscdefs
import subprocess
from tapas_sumo_coupling import database

updateCmd = ["UPDATE public.simulation_parameters SET sim_key='2015y_05m_29d_09h_01m_11s_943ms';",
             "UPDATE public.simulation_parameters SET param_value='test_trips' WHERE param_key='DB_TABLE_TRIPS';",
             "UPDATE public.simulation_parameters SET param_value='1' WHERE param_key='SUMO_MAX_ITERATION';",
             "UPDATE public.global_sumo_status SET sim_key='2015y_05m_29d_09h_01m_11s_943ms';"]

os.chdir("data")
database.start(tscdefs.testServer, tscdefs.get_python_tool("tsc_main.py") + ['--limit', '50000'], [open('initialState.sql'), updateCmd], [], [])