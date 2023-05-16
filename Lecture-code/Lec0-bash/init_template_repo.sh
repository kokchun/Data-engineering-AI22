#!/bin/bash

#!/bin/bash

echo "running initializations for this repo" 
sleep 1
mkdir theory code-alongs explorations  
touch theory/.gitkeep code-alongs/.gitkeep

for i in {1..5}; do
    echo "This is file $i" >> file$i.txt
done
