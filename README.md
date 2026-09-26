# Cybersecurity Vulnerability Testing Suite

## Overview
This repository contains a comprehensive suite of Python-based Proof-of-Concept (PoC) scripts and testing tools designed to analyze and expose logical vulnerabilities within a custom stateful TCP client-server application (named "Glitter"). 

The project was developed as part of a security research assignment to systematically investigate network protocols, reverse-engineer backend behaviors, and automate vulnerability exploitation based on the STRIDE threat model.

## Features & Capabilities
*   **Protocol Analysis:** Tested a custom text-based protocol over TCP (Port 1336).
*   **Automated Testing:** Python scripts engineered to manipulate data parameters and automate requests.
*   **Vulnerability Identification:** Successfully identified and documented various backend logic flaws, including:
    *   **Tampering & Spoofing:** Unauthorized actions (e.g., modifying likes/comments of other users, spoofing avatars).
    *   **Information Disclosure:** Extracting hidden user IDs and private data via search and settings parameters.
    *   **Input Validation Failures:** Exposing lack of server-side validation (e.g., missing character limits, accepting empty inputs, injecting past/future timestamps).

## Methodology
The testing process was divided into systematic entry point investigations (e.g., likes, comments, user registration, settings updates). For each entry point, multiple scenarios were tested to determine if the server could be manipulated into performing unintended actions or disclosing sensitive data.

## Technologies Used
*   **Python:** Core language used for writing all automated testing scripts and networking interactions.
*   **Networking:** Stateful TCP communication analysis.

## Note on Usage
*Disclaimer: This suite was developed strictly for educational purposes and authorized security research as part of an academic program. The tools are designed to demonstrate specific logic flaws and should not be used maliciously.*