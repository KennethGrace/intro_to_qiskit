# via Qiskit, we will write a Quantum Teleportation Algorithm. ALRIGHT, so, a qubit, q0, is set to some initial state, then the information in q0 is 'copied' to q2 (copying is impossible in quantum computing, so the information must be telported, this is what is meant by quantum teleportation). Pretty dope.
# %% import qiskit library, as well as the plotting tools, and an exception hander
import sys
import math
from qiskit import *
from qiskit.tools.visualization import plot_histogram
from qiskit.tools.monitor import job_monitor
from qiskit.providers.ibmq.job.exceptions import *
# %% set wether to use Aer or IBMQ
use_ibmq = True
# %% build the quantum circuit
circuit = QuantumCircuit(3, 3)
# %% draw the circuit as initialized
circuit.draw()
# %% apply an initial state to q1, and draw
circuit.x(0)
circuit.barrier()
circuit.draw()
# %% hadamard on q1 and conditional x on q2 based on q1
# this entangles q1 and q2, draw the resulting circuit
circuit.h(1)
circuit.cx(1, 2)
circuit.draw()
# %% conditional x on q1 based on q0, hadamard on q0
# we expect now, that TODO... I think re-hadamard on
# q0 is counter productive, but i also, have no idea
# what i am doing, still leaving it out.
circuit.cx(0, 1)
circuit.h(0)
circuit.draw()
# %% teleport the information in q0 to q2, then draw
circuit.barrier()
circuit.cx(1, 2)
circuit.cz(0, 2)
circuit.draw()
# %% measure both registers for validation of teleportation, then draw
circuit.measure([0, 1, 2], [0, 1, 2])
circuit.draw()
# %% run this circuit using the specified backend
if use_ibmq:
    try:
        IBMQ.load_account()
        provider = IBMQ.get_provider('ibm-q')
        qcomp = provider.get_backend('ibmq_16_melbourne')
        job = execute(circuit, backend=qcomp, shots=2048)
        job_monitor(job)
        result = job.result()
    except IBMQJobFailureError:
        print('Job Failed with Below Error')
        print(job.error_message())
        sys.exit(0)
else:
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(circuit, backend=simulator, shots=2048).result()
# %% print the raw results to a histogram
counts = result.get_counts(circuit)
plot_histogram(counts)
# %% print the raw data for the results
print(counts)
# %% process the data to only care about c2
data = {'1': 0, '0': 0}
for r, c in counts.items():
    data['1'] += c if r.startswith('1') else 0
    data['0'] += c if r.startswith('0') else 0
# %% draw a histogram of the resulting data
plot_histogram(data)
# %% print the processed data
print(data)
