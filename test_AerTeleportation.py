# via Qiskit, we will write a Quantum Teleportation Algorithm. ALRIGHT, so, a qubit, q0, is set to some initial state, then the information in q0 is 'copied' to q2 (copying is impossible in quantum computing, so the information must be telported, this is what is meant by quantum teleportation). Pretty dope.
# %% import qiskit library, as well as the plotting tools
from qiskit import *
from qiskit.tools.visualization import plot_histogram, plot_bloch_multivector
# %% build the quantum circuit
circuit = QuantumCircuit(3, 3)
# %% draw the circuit as initialized
circuit.draw(output='mpl')
# %% apply an initial state to q1, and draw
circuit.x(0)
circuit.barrier()
circuit.draw(output='mpl')
# %% hadamard on q1 and conditional x on q2 based on q1
# this entangles q1 and q2, draw the resulting circuit
circuit.h(1)
circuit.cx(1, 2)
circuit.draw(output='mpl')
# %% conditional x on q1 based on q0, hadamard on q0
# we expect now, that TODO... I think re-hadamard on
# q0 is counter productive, but i also, have no idea
# what i am doing, still leaving it out.
circuit.cx(0, 1)
circuit.h(0)
circuit.draw(output='mpl')
# %% measure q0 and q1 and assign them to c0 and c1. draw
circuit.barrier()
circuit.draw(output='mpl')
# %% teleport the information in q0 to q2, then draw
circuit.barrier()
circuit.cx(1, 2)
circuit.cz(0, 2)
circuit.draw(output='mpl')
# %% measure q2 to c2 for validation of teleportation,
# then draw
circuit.draw(output='mpl')
# %% simulate this circuit using Aer
simulator = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend=simulator).result()
# %% print the results to a bloch vector
statevector = result.get_statevector()
plot_bloch_multivector(statevector)
# %% print the raw results to a histogram
counts = result.get_counts()
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
