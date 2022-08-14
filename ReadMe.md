## Market Research and Analysis
### using web-crawling and sentiment analysis
#
The module was made with the intention to automate the process of equity analysis and market fundamentals from public data and analyze sentiments.

![Market Research](https://wp.disruptiveadvertising.com/wp-content/uploads/2018/10/market-research-blog.jpg)


#### Steps to be followed
1.  ```console
    $ python3 ./google_search_and_save.py
    ```
    the data from google search will be scrapped and stored under data folder in the form of .html files and will give out token based on which the data can be scrapped in next step.

2. ```console
    $ python3 ./scrap_data.py <token>
    ```
    above command will scrap data from saved .html file and will convert data into .csv file that can be used for furthur sentiment analysis

