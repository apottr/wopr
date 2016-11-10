### WOPR
===
## Files
 - server.py
 - objects.py
 - geo.py
 - objects/*.json

## Executive Summary
WOPR is a War Simulator. Currently set up to simulate global thermonuclear war between Soviet Russia and the United States like it's namesake, it will be able to be modified to facilitate simulations ranging from localized intranational squabbles to total global international war.

## Summaries
# server.py
This file contains all server logic, handling of API keys and REST communication.
It also generates telemetry data and status information. It manages interaction between all other files.

# geo.py
This file contains all geospatial logic and processing. It is essential for determining what is where.

# objects.py
This file manages all JSON objects and allows files to query objects by name and ID.

# objects/*.json
These files contain object information for each available object in the system.
