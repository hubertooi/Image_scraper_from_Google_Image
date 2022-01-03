# Image Scraper on Google Images
I use selenium chrome webdriver for this to work.
You just need to download it and use the code.
The one thing to note is the chromedriver has to be downloaded from this website: https://chromedriver.chromium.org/downloads

I will need to give credit to Eshita Goel's post on medium where I modified to code for this to work.
Here is the link: https://medium.com/geekculture/scraping-images-using-selenium-f35fab26b122

## Things to take note
* You will need to download a specific ChromeDriver version similar to your Chrome version on your laptop or desktop
* I am using the ChromeDriver 96.0.4664.45 version since my Chrome version on my windows is 96.0.4664.110
* It does not need to matched entirely, but the first 2 digit must matched
* Once downloaded, make sure you do not rename chromedriver.exe and place it within the same folder of the python code.
* You can specify the image name you want to scrape, the number of images you want, and the delay time for selenium to click on the google images.
* Make sure the delay time is not too brief!
* Make sure to use pip to install needed packages for the code to work, these packages' name are on the requirement.txt file.

## Wish you all the best and happy New Year and happy scraping!!!