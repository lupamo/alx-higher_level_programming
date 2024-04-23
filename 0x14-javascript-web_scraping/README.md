# JavaScript - Web scraping

Web scraping in JavaScript involves extracting data from websites programmatically. This process is essential for various applications, including data analysis, price comparison, content aggregation, and more. JavaScript, being a versatile programming language that runs in the browser, is an excellent choice for web scraping due to its ability to interact with web pages directly.

## Tools and Libraries

- Puppeteer: A high-level browser automation library that allows you to programmatically control web applications as if a real person were interacting with them. It's useful for tasks that require interaction with the webpage, such as clicking buttons or navigating through pages
- Cheerio: Similar to jQuery, Cheerio is used for server-side web scraping. It parses HTML and XML documents and provides an API for traversing/manipulating the resulting data structure. However, it does not execute JavaScript code
- JSDOM: Creates a DOM per the standard JavaScript specification out of an HTML string, allowing you to perform DOM manipulations on it. This is useful for parsing and manipulating HTML documents in a Node.js environment
- Axios, SuperAgent, node-fetch, and Request: These are HTTP clients used to send HTTP requests to a server and receive a response. They are essential for fetching the content of a site, which is the first step in any scraping project 
