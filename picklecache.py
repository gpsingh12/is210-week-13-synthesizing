#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create an object that can get, set aand delete other pickled
   python objects to and from a file."""

import os
import pickle


class PickleCache(object):
    """ Object is parent class for PickleCache.
    Attributes:
        None
    """
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Constructor function for PickleCache.
        Args:
            file_path(str): defaults to datastore.pkl
            autosync(bool): defaults to False.
        Attributes:
            file_path(str): assigned the constructor variable __file_path value
            autosync(bool): non private attribute
            __data(dict): an empty dictionary object.
        """
        self.__file_path = file_path
        self.autosync = autosync
        self.__data = {}
        self.load()

    def __setitem__(self, key, value):
        """Function takes two arguments and save in a dictionary.
        Args:
            key(str): input arg.
            value(str): input arg.
        Return:
            returns the saved values in a dictionary.
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache._PickleCache__data['test']
            'hello'
            >>> len(pcache)
            1
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """Function takes no argument.
        Args:
            None
        Return:
            returns the length of self.__data
        Examples:
            >>> pcache = PickleCache
            >>> pcache['test'] = 'hello'
            >>> len(pcache)
            1
        """
        return len(self.__data)

    def __getitem__(self, key):
        """Function takes one argument.
        Args:
            key(mixed): dictionary key to access data
        Return:
            returns the key or raise an error if key is not found
        Examples:
            >>> pcache = PickleCache()
            >>> pcache['test'] = 'hello'
            >>> print pcache['test']
            hello
            >>> print pcache['exam']

            Traceback (most recent call last):
             File "<pyshell#5>", line 1, in <module>
            print pcache['exam']
            File "/home/vagrant/Desktop/is210-week-13-synthesizing/
            picklecache.py", line 78, in __getitem__
            raise KeyError('key not found')
            KeyError: 'key not found'
        """
        try:
            return self.__data[key]
        except KeyError:
            raise KeyError('key not found')

    def __delitem__(self, key):
        """Function deletes the entries.
            Args:
                key(mix): a dictionary key used to remove the entries.
            Return:
                returns the dict after deleting the items accessed by key.
            Examples:
                >>> pcache = PickleCache()
                >>> pcache['test'] = 'hello'
                >>> del pcache['test']
                >>> len(pcache)
                0
        """
        del (self.__data)[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """Function load the file object and save contents in self.__data
        Args:
            None
        """
        if os.path.exists(self.__file_path)\
           and os.path.getsize(self.__file_path) > 0:
            fhandler = open(self.__file_path, 'r')
            self.__data = pickle.load(fhandler)
            fhandler.close()

    def flush(self):
        """Function open the file as writable and dump to save the data
            to file object.
        Args:
            None
        """
        fhandler = open(self.__file_path, 'w')
        pickle.dump(self.__data, fhandler)
        fhandler.close()
