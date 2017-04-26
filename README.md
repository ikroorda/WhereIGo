# WhereIGo

1. Go to [Google Takeout](https://takeout.google.com/settings/takeout) and select only Location History: JSON format
2. Download the .json file and formate to include only desired timestamps
  * By hand, use [epoch converter](https://www.epochconverter.com/) to find the chunk of lat/long data for your target dates and save to a new file
  * Clean up the start, end so it resembles example .json format
3. Run mapit.py
4. Open overall.html

TODO:
   * faster dot-mapping rather than line-mapping with color gradient
   * heat mapping
   * automatic date-selector
   * auto zoom and centering
