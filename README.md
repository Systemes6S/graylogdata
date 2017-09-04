# GrayLogData Scripts
A python scripts to import and export an index from ElasticSearch node to another one. You can use theses scripts for backup too.

Theses scripts create an archive file SVG_index_xxx.tar.bz2

# How to use GrayLogDataExporter.py ?

1. Run the GrayLogDataExporter.py script:

```
./GrayLogDataExporter.py
```

2. Indicate the name of the index to be exported:

```
Name of index to export: index_xxx
```

```python
Name of index to export: index_xxx
Closing index_xxx [OK]
Creating the archive: SVG_index_xxx.tar.bz2 [OK]
Opening the Index index_xxx [OK]

Hash : 2b39c58e54c709a6bb61f62d42c43ed2
```

The hash makes it possible to verify when copying on the other server that the archive is integral.

3. You can copy the archive file SVG_index_xxx.tar.bz2 on a backup server for example.

# How to use GrayLogDataImporter.py ?

1. Upload your index file .tar.bz2 in the same folder of script and run the GrayLogDataImporter.py script:

```
./GrayLogDataImporter.py
```

2. Specify the name of the index to be imported:

```
Name of index to import: index_xxx
```

3. Check that the hash corresponds to the one that was specified during export:

```python
Hash the archive: 2b39c58e54c709a6bb61f62d42c43ed2
Decompressing the archive [OK]
Stopping elasticsearch: [OK]
Starting elasticsearch: [OK]
Opening the Index index_xxx [OK]
```

5. Verify that ElasticSearch confirms that everything went smoothly and does not detect any problems (visible in the GrayLog web interface)
