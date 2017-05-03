# QuantumNotes
Lecture notes for Scott Aaronson's [CS378 Quantum Information Science](http://www.scottaaronson.com/cs378/) at UT Austin, Spring 2017



#### [Lecture 1 (January 17)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_1.pdf)


An introduction to Quantum Information Science. A few important concepts are introduced (**Probability**, **Locality**, **Local** **Realism**, the **Church-Turing Thesis** and its extended variation) to contextualize how quantum mechanics affects our understanding of physics.

#### [Lecture 2 (January 19)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_2.pdf)

Quantum mechanics challenges **Computational Universality**.

The **Double Slit Experiment** introduces **Decoherence** and **Interference**. It motivates us to use **Amplitudes** to measure quantum chance, which are related to probabilities through the **Born Rule**.
Linear Algebra can model classical probabilities using **Stochastic Matrices** and **Tensor Products**.

#### [Lecture 3 (January 24)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_3.pdf)

**Quantum States** and the **Qubit** warrant using **Bra-Ket Notation**. Linear Algebra can model quantum states too, but for that we need **Unitary** and **Orthogonal** **Matrices**, as well as **Unitary Transformations**.

#### [Lecture 4 (January 26)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_4.pdf)

Several examples of **Quantum Gates** get us working in multiple bases. The compatibility (or lack thereof) between **Unitary Transformations** and **Measurement** is explored. **Quantum Circuit Notation** is introduced, along with phenomena occurring with a single qubit (**Quantum Zeno Effect**, **Watched Pot Effect**, **Elitzur-Vaidman Bomb**).

#### [Lecture 5 (January 30)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_5.pdf)

Our first quantum protocol distinguishes between a fair and biased coin. The distinguishability of quantum states is explored.

Considering the state of two qubits with linear algebra and quantum circuit notation introduces the **Partial Measurement Rule**, the **Controlled NOT**, and the **Bell Pair**. **Entanglement** comes into play, and we see why it need not require the existence of faster-than-light communication.

#### [Lecture 6 (February 2)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_6.pdf)

**Density Matrices** are introduced to represent **Mixed States**. We see the properties of density matrixes including **Trace** and **Rank**, as well as processes we may want to do with them like applying unitary transformations, performing **Eigendecomposition**, and **Tracing Out**.

#### [Lecture 7 (February 7)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_7.pdf)

The **Bloch Sphere** is introduced as a useful representation of possible states of a qubit.
￼￼￼￼￼￼￼
￼The **No Communication Theorem** and the **No Cloning Theorem** limit what can be done with quantum information. These limits allow for the creation of **Quantum Money** schemes, such as **Wiesner’s Scheme**.

#### [Lecture 8 (February 9)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_8.pdf)

Attacks on Wiesner’s Scheme are explored, including an **Interactive Attack**, and an **Attack Based on the Elitzur Vaidman Bomb**.

**BB84** is a **Quantum Key Distribution** scheme allowing two parties to generate a shared secret.

#### [Lecture 9 (February 14)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_9.pdf)

Using entanglement as a resource allows for **Superdense Coding**, transmitting two classical bits via one qubit, and **Quantum Teleportation**, transmitting a qubit via classical communication.

#### [Lecture 10 (February 16)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_10.pdf)

Quantum Teleportation is further explored and extended to arbitrary quantum states. Quantifying entanglement leads us to **Entanglement Swapping**, the **GHZ State** and the **Monogamy of Entanglement**, as well as **Schmidt Decomposition**.

#### [Lecture 11 (February 21)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_11.pdf)

Measuring entropy of a quantum state with **Von Neumann Entropy** and **Entanglement Entropy**. The **Measurement Problem** leads us into interpretation of quantum mechanics, the **Copenhagen Interpretation** and **S.U.A.C.**, as well as useful though experiments, **Schrödinger’s Cat** and **Wigner’s Friend**.

#### [Lecture 12 (February 23)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_12.pdf)

**Dynamic Collapse** theories such as **GRW** and the **Penrose Interpretation** suggest that we’re still missing part of the puzzle. **Everett’s Many Worlds Interpretation** suggests that the universe branches every time a measurement happens.

#### [Lecture 13 (February 28)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_13.pdf)

A further discussion of Many Worlds tackles the practicality of an unfalsifiable interpretation and the **Prefered Basis Problem**.

**Hidden Variable Theories** such as **Bohmian Mechanics** lead to a search for a local hidden variable theory which proves to be impossible given the **Bell Inequality**, leading us to the **CHSH Game**.

#### [Lecture 14 (March 2)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_14.pdf)

The optimality of our strategy for the CHSH Game is discussed and proven through **Tsirelson’s Inequality**. The implications of experimentally **Testing the Bell Inequality** lead us to **Superdeterminism** and modern skepticism of quantum mechanics.

Other non-local games (**The Odd Cycle Game** and **The Magic Square Game**) are covered.
2
￼￼￼￼￼￼￼
#### [Lecture 15 (March 9)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_15.pdf)

The CHSH Game can be applied to **Generating Guaranteed Random Numbers**, and many other tasks, which brings us to **Quantum Computing**. We discuss the intellectual origins of the field and a few conceptual points.

#### [Lecture 16 (March 21)](https://github.com/saNed/QuantumNotes/blob/master/IndividualLectures/Lecture_16.pdf)

The roles of interference and entanglement in quantum computing lead us to cover the construction of both classical and quantum **Universal Gate Sets**. We discuss **Quantum Complexity** and see our first quantum algorithm, **Deutsch’s Algorithm**.
