
if [ $# -ne 1 ]
then
   echo "Enter count of images:"
   exit 1
fi

export COUNT=$1
cd  /home/azureuser/val2017
ls | head -$COUNT > input.txt

for i in `cat /home/azureuser/val2017/input.txt`; do cp /home/azureuser/val2017/${i} /home/azureuser/dikshith/input/; done

echo "Source location - /home/azureuser/val2017/"
echo "Destination location - /home/azureuser/dikshith/input"

