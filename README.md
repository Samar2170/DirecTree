# USAGE


## Installation
    
    ```bash
    pip install -i https://test.pypi.org/simple/ directree
    ```

### Get an Idea of how many files are in their in the directory with their sizes
    
    ```bash
    directree ./directory/ -fs
    ```

    ```
    Type     Files           Size       
    images   7               3827.6279296875 Kb 
    txt      2               9.34765625 Kb 
    spreadsheets 58              579.6826171875 Kb 
    pdf      10              1235.1943359375 Kb 
    other    12              5162.6572265625 Kb 
    ```
    

### Count Lines of Code and Files by language type in a repo
        
    ```bash
    directree ./directory/ -c
    ```

    ```
    Lang     Files           LOCs       
    python   2108            342359     
    json     3               3          
    xml      1               15         
    bash     1               16         
    other    2005            113136 
    ```


### Print a directory Tree

    ```bash
    directree ./directory/ -t
    ```

    ```
    test/
    |
    ├──tes1/
    |  └──sample.py
    |
    └──sample.py
    ```
