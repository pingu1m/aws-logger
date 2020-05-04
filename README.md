# AWS Cloud Logger

## Usage:

### Generate Config
```shell script
# Generate Config sample
clog config -g -> config-sample
# Rename file to be read by script
mv config-sample .clogrc
```
#### Config vars
- One
- Two

### Get log single item
```shell script
clog get -s aurora -t tablename -i 23234
```

### Get log list
```shell script
clog ls -s aurora -t tablename
clog ls -s dyname -t tablename -q 'querystring'
```

### Add log item
```shell script
clog put  -s aurora -t tablename filelike_content
```

### Add log item thru file
```shell script
clog put  -s aurora -t tablename -f filename
# this will add each line as one item
```

### Truncate a table
```shell script
clog config -s aurora -t tablename --truncate 
# By default it dry-run is enabled
# To run the mentioned command use the --run flag
clog config -s aurora -t tablename --truncate --run
```

### Seed a table
```shell script
clog config -s aurora -t tablename --seed < script_name
# By default it dry-run is enabled
# To run the mentioned command use the --run flag
clog config -s aurora -t tablename --seed --run < script_name
```

### Dump a table
```shell script
clog config -s aurora -t tablename --dump 
```

### 


### Flags

- -s/--storage "aurora", "dynamo"
- -t/--tabla   
- -i/--id      
- -v/--verbose 
- -h/--help    
- -q/--query   

    