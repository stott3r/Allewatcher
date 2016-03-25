from suds.client import Client


class Allegro:
    def __init__(self):
        self.webapi_key = 'f8e0c860'  # delete this before upload to github
        self.country = 1
        self.client = Client('https://webapi.allegro.pl/service.php?wsdl')
        self.client.options.cache.setduration(hours=2)

    # gets category list from webapi

    def get_categories(self):
        category_list = self.client.service.doGetCatsData(
            countryId=self.country,
            webapiKey=self.webapi_key
        ).catsList.item

        categories = []
        for item in category_list:
            categories.append({'id': item.catId, 'name': item.catName, 'parent': item.catParent})

        return categories

    # search for free only, with time fixed at 24h. User can set phrase and category only.

    def search(self, category, phrase, interval):
        params = [{
            'item': ({'filterId': 'category', 'filterValueId': {'item': category}},
                     {'filterId': 'startingTime', 'filterValueId': {'item': interval}},
                     {'filterId': 'search', 'filterValueId': {'item': phrase}})
        }]
        search_raw_result = self.client.service.doGetItemsList(
            countryId=self.country,
            webapiKey=self.webapi_key,
            filterOptions=params,
        ).itemsList.item

        search_result = []

        for item in search_raw_result:
            search_result.append({'id': item.itemId, 'name': item.itemTitle,
                                  'type': item.priceInfo.item[0].priceType, 'price': item.priceInfo.item[0].priceValue})

        return search_result
