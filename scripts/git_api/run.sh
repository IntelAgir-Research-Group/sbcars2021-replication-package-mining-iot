# extraction_script filename where_to_look terms start_result_index username hash
username=
hash=
# DESCRIPTION
./extract.sh internet_thing_robot description internet+thing+robot 1 $username $hash
./extract.sh iort description iort 1 $username $hash
./extract.sh internet_thing description internet+thing 1 $username $hash
./extract.sh iot description description iot 1 $username $hash
# TITLE
./extract.sh internet_thing_robot title internet+thing+robot 1 $username $hash
./extract.sh iort title iort 1 $username $hash
./extract.sh internet_thing title internet+thing 1 $username $hash
./extract.sh iot description title iot 1 $username $hash

