class WebScraper:
    def __init__(self, collection, venue):
        self.collection = collection
        self.venue = venue

    def run(self):
        self.venue.run()
        data = self.venue.write_data()
        print(f'data from run: {data}')
        self.collection.insert_one(data)
