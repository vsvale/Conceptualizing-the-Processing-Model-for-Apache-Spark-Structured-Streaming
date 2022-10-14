# Conceptualizing-the-Processing-Model-for-Apache-Spark-Structured-Streaming


### Notes
#### WordCount
- sudo apt-get update; sudo apt-get install netcat -y;
- nc -lk 9999
- pip install pyspark
- spark-submit word_count.py localhost 9999
- Insert in nc console:
```
A stream is a continuous body of surface water flowing within the bed and banks of a channel. Depending on its location or certain characteristics, a stream may be referred to by a variety of local or regional names. Long large streams are usually called rivers, while smaller, less voluminous and more intermittent streams are known as streamlets, brooks or creeks.
The flow of a stream is controlled by three inputs – surface runoff (from precipitation or meltwater), daylighted subterranean water, and surfaced groundwater (spring water). The surface and subterranean water are highly variable between periods of rainfall. Groundwater, on the other hand, has a relatively constant input and is controlled more by long-term patterns of precipitation. The stream encompasses surface, subsurface and groundwater fluxes that respond to geological, geomorphological, hydrological and biotic controls.
Streams are important as conduits in the water cycle, instruments in groundwater recharge, and corridors for fish and wildlife migration. The biological habitat in the immediate vicinity of a stream is called a riparian zone. Given the status of the ongoing Holocene extinction, streams play an important corridor role in connecting fragmented habitats and thus in conserving biodiversity. The study of streams and waterways in general is known as surface hydrology and is a core element of environmental geography.
```

#### Happiness score
- sudo apt-get update; sudo apt-get install netcat -y;
- nc -lk 9999
- pip install pyspark
- spark-submit happiness_score.py localhost 9999
- Insert in nc console:
```
    Denmark WesternEurope 7.526
    Peru LatinAmericaandCaribbean 5.743
    Switzerland WesternEurope 7.509
```

#### Yahoo Finance
- move files from original_stock_data to stock_data
- pip install pyspark
- spark-submit append_mode.py
- spark-submit append_mode_view.py
- spark-submit complete_mode.py
- spark-submit complete_mode_agg.py
- spark-submit update_mode.py
- spark-submit update_mode_sql.py
- spark-submit schema_inference.py
- spark-submit checkpointing.py
- spark-submit continuous_processing.py
- spark-submit broadcast.py
- spark-submit accumulator.py
- spark-submit udfs.py
- spark-submit udfs_sql.py