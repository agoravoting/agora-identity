# -*- coding: utf-8 -*-
# Copyright (C) 2014 Eduardo Robles Elvira <edulix AT agoravoting DOT com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# Forms for the base application
#

from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100)
    nickname = forms.CharField(max_length=100)
    password = forms.CharField()
    password2 = forms.CharField()