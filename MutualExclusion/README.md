## Running

Run the docker compose file

    $ sudo docker compose up

Wait until the lock manager starts, then run the clients containers

    $ sudo bash run.bash

You can see the logs of lock_manager container

    $ sudo docker ps -a
    $ sudo docker logs -f (mutualexclusion-lock-manager or it ID)