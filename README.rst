====================
Test Checker Backend
====================

.. image:: https://github.com/bigcrazyfrog/test-checker-backend/actions/workflows/checks.yaml/badge.svg
   :target: https://github.com/bigcrazyfrog/test-checker-backend/actions/
.. image:: https://github.com/bigcrazyfrog/test-checker-backend/actions/workflows/deploy.yaml/badge.svg
   :target: https://github.com/bigcrazyfrog/test-checker-backend/actions/

Setup localy
------------

.. code-block:: bash

    git clone https://github.com/bigcrazyfrog/test-checker-backend.git

Create ``.env`` file from ``.env.example``.

Create docker images and execute the containers for development. Use commands from `Makefile`:

.. code-block:: bash

    make up
