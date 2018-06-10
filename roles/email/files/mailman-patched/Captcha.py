# Copyright (C) 2018 by Ralf Jung
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA.

import random
from Mailman import Utils

def display(mlist, captchas):
    """Returns a CAPTCHA question, the HTML for the answer box, and
    the data to be put into the CSRF token"""
    idx = random.randrange(len(captchas))
    question = captchas[idx][0]
    box_html = mlist.FormatBox('captcha_answer', size=30)
    return (Utils.websafe(question), box_html, str(idx))

def verify(idx, given_answer, captchas):
    try:
        idx = int(idx)
    except ValueError:
        return False
    if not idx in range(len(captchas)):
        return False
    # Chec the given answer
    correct_answers = captchas[idx][1]
    given_answer = given_answer.strip().lower()
    return given_answer in map(lambda x: x.strip().lower(), correct_answers)
