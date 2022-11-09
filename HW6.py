import json
import unittest
import os
import requests

#
# Your name:
# Who you worked with:
#

# Make sure you create an API key at https://developer.nytimes.com/apis; see instructions

API_KEY = ""

def read_json(cache_filename):
    '''
    Loads a JSON cache from cache_filename if it exists

    Parameters
    ----------
    cache_filename: string
        the name of the cache file to read in

    Returns
    -------
    dict
        if the cache exists, a dict with loaded data
        if the cache does not exist, an empty dict
    '''
    pass

def write_json(cache_filename, dict):
    '''
    Encodes dict into JSON format and writes
    the JSON to cache_filename to save the search results

    Parameters
    ----------
    cache_filename: string
        the name of the file to write a cache to
    
    dict: cache dictionary

    Returns
    -------
    None
        does not return anything
    '''  
    pass
    

def get_request_url(list):
    '''
    Builds a request url for an API call

    NOTE: consider using a formatted string (f-string)!

    Parameters
    ----------
    list: str
        a string of the name of the best seller list to search in the Books API. ex: hardcover-fiction

    Returns
    -------

    str
        a search url for the Books API

        NOTE: Set the date to July 10th, 2016 (2016-07-10).

        Example of a request URL for hardcover fiction: https://api.nytimes.com/svc/books/v3/lists/2016-07-10/hardcover-fiction.json?api-key=API_KEY

    '''
    pass

def get_data_using_cache(list, cache_filename):
    '''
    Uses the passed search generate a request_url using
    the 'get_request_url' function

    If url is found in the dict return by `read_json`, prints
    "Using cache for {list}" and returns the url results

    If url is not found in the dict return by `read_json`, prints
    "Fetching data for {list}" and makes a call to Books API to
    get the data the search

    If request is successful, add the data to a dictionary (key is
    the request_url, and value is part of the results) and writes
    out the dictionary to cache using `write_json`

    Parameters
    ----------
    list: str
        a string the name of the best seller list to search in the Books API. ex: hardcover-fiction
    cache_filename: str
        the name of the file to write a cache to
    
    Returns
    -------
    url result:
        results of a url request either from the cache or website
    None:
        if search is unsuccessful
    '''
    pass

def most_weeks(cache_filename):
    '''
    reads the cache file and finds the book that has been on the list 
    for the most weeks and returns a dictionary with the list name as 
    the key and the title of the book as the value.

    Parameters
    ----------
    cache_filename: str
        the name of the cache file to read from

    Returns
    -------
    dict
        a dictionary {list_name1: title1, list_name2: title2}
    '''
    pass

#######################################
############ EXTRA CREDIT #############
#######################################

def get_best_seller_brothers(cache_filename):
    '''
    reads the cache file and looks for the two brothers that share the last 
    name Goldberg in the best sellers list for Hardcover Fiction and returns 
    a nested dictionary: {authors’ names: {rank of the book: title of the book}, …}

    Parameters
    ----------
    cache_filename
        the name of the cache to read
    
    Returns
    -------
    dict
        a nested dictionary
    '''
    pass


####################
#### TEST CASES ####
####################

class TestHomework6(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.cache_filename = dir_path + '/' + "cache_bestseller.json"
        self.list_name = ["hardcover-fiction", "hardcover-nonfiction", "e-book-fiction", "e-book-nonfiction", "combined-print-and-e-book-fiction", "combined-print-and-e-book-nonfiction"]
        self.cache = read_json(self.cache_filename)
        self.API_KEY = API_KEY

    def test_write_json(self):
        write_json(self.cache_filename, self.cache)
        dict1 = read_json(self.cache_filename)
        self.assertEqual(dict1, self.cache)

    def test_get_request_url(self):
        for m in self.list_name:
            self.assertIn("api-key={}".format(self.API_KEY),get_request_url(m))
            self.assertIn("{}".format(m),get_request_url(m))

    def test_get_data_using_cache(self):
        for m in self.list_name:
            dict_returned = get_data_using_cache(m, self.cache_filename)
            if dict_returned:
                self.assertEqual(type(dict_returned), type({}))
                self.assertIn(get_request_url(m),read_json(self.cache_filename))
            else:
                self.assertIsNone(dict_returned)

    def test_most_weeks(self):
        # IMPLEMENT
        pass

    def test_get_best_seller_brothers(self):
        self.assertEqual(get_best_seller_brothers(self.cache_filename), {'Janet Evanovich and Lee Goldberg': {8: 'THE PURSUIT'}, 'Brad Meltzer and Tod Goldberg': {16: 'THE HOUSE OF SECRETS'}})

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cache_filename = dir_path + '/' + "cache_bestseller.json"

    list_names = ["hardcover-fiction", "hardcover-nonfiction", "combined-print-and-e-book-nonfiction"]
    [get_data_using_cache(list, cache_filename) for list in list_names]
    print("________________________")
    # Fetch the data for E-Book Nonfiction
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_using_cache('e-book-nonfiction', cache_filename)
    data2 = get_data_using_cache('e-book-nonfiction', cache_filename)
    print("________________________")

    # Getting the data for E-Book Fiction
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_using_cache('e-book-fiction', cache_filename)
    data2 = get_data_using_cache('e-book-fiction', cache_filename)
    print("________________________")

    # Getting the data for Combined Print and E-Book Fiction
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_using_cache('combined-print-and-e-book-fiction', cache_filename)
    data2 = get_data_using_cache('combined-print-and-e-book-fiction', cache_filename)
    print("________________________")

    print("Get book that has been on the best seller list for the most weeks ")
    print(most_weeks(cache_filename))
    print("________________________")


    # Extra Credit
    # Keep the statements commented out if you do not attempt the extra credit
    print("EXTRA CREDIT!")
    # itunes_list() function does not take any parameters.
    print(get_best_seller_brothers(cache_filename))
    print("________________________")
    
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)
