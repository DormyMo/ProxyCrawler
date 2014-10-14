import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'xici'])

if  __name__ =='__main__':
    main()