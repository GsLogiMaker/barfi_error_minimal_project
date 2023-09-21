
import streamlit as st
import barfi as bf

node = bf.Block("Node")
node.add_input("Input1", value="")
node.add_input("Input2", value=[])
node.add_output("Output", value=[])

"Create two nodes and connect their outputs to the other's inputs and click Excecute."
"The result is 'TypeError: exceptions must derive from BaseException'"
"This should raise a custom error, maybe named CyclicConnectionError"
bf.st_barfi([node])