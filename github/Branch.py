# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import github.GithubObject

import github.Commit


class Branch(github.GithubObject.BasicGithubObject):
    """
    This class represents Branchs as returned for example by http://developer.github.com/v3/todo
    """

    @property
    def commit(self):
        """
        :type: :class:`github.Commit.Commit`
        """
        return self._NoneIfNotSet(self._commit)

    @property
    def name(self):
        """
        :type: string
        """
        return self._NoneIfNotSet(self._name)

    def _initAttributes(self):
        self._commit = github.GithubObject.NotSet
        self._name = github.GithubObject.NotSet

    def _useAttributes(self, attributes):
        if "commit" in attributes:  # pragma no branch
            assert attributes["commit"] is None or isinstance(attributes["commit"], dict), attributes["commit"]
            self._commit = None if attributes["commit"] is None else github.Commit.Commit(self._requester, attributes["commit"], completed=False)
        if "name" in attributes:  # pragma no branch
            assert attributes["name"] is None or isinstance(attributes["name"], (str, unicode)), attributes["name"]
            self._name = attributes["name"]
