# %%
import qiskit as q
# %%
qr = q.QuantumRegister(2)
# %%
cr = q.ClassicalRegister(2)
# %%
circuit = q.QuantumCircuit(qr, cr)
# %%
%matplotlib inline
# %%
circuit.draw()
