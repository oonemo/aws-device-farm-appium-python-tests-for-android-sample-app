# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/apache2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from tests.pages.base_pages.base_page import BasePage


class NestedViewsPage(BasePage):
    """Nested views page representation."""
    UP_NAVIGATION_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/nested_up_button'
    BACK_NAVIGATION_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/nested_back_button'
    FIRST_LEVEL_TEXT_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/up_navigation_content_text'
    FINAL_LEVEL_TEXT_CLASS_NAME = 'android.widget.TextView'
    UP_NEXT_LEVEL_BUTTON_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/nested_up_button'
    BACK_NEXT_LEVEL_BUTTON_ID = 'com.amazonaws.devicefarm.android.referenceapp:id/back_navigation_next_button'
    COUNTER_ACCESSIBILITY_ID = 'Level Display'
    UP_NAVIGATION_BACK_BUTTON_ACCESSIBILITY_ID = 'Navigate up'

    def press_up_navigation(self):
        """Press up navigation button."""
        up_navigation = self.driver.find_element_by_id(self.UP_NAVIGATION_ID)
        up_navigation.click()

    def press_back_navigation(self):
        """Press back navigation button."""
        back_navigation = self.driver.find_element_by_id(self.BACK_NAVIGATION_ID)
        back_navigation.click()

    def first_level_text_is_displayed(self):
        """Returns visibility of first level text as a boolean."""
        first_level_text = self.driver.find_element_by_id(self.FIRST_LEVEL_TEXT_ID)
        return first_level_text.is_displayed()

    def final_level_text_is_displayed(self):
        """Returns visibility of final level text as a boolean."""
        final_level_text = self.driver.find_element_by_class_name(self.FINAL_LEVEL_TEXT_CLASS_NAME)
        return final_level_text.is_displayed()

    def press_up_navigation_back_button(self):
        """Press up navigation back button."""
        back_button = self.driver.find_element_by_accessibility_id(self.UP_NAVIGATION_BACK_BUTTON_ACCESSIBILITY_ID)
        back_button.click()

    def press_back_next_level(self):
        """Press back nabigation next level button."""
        next_level_button = self.driver.find_element_by_id(self.BACK_NEXT_LEVEL_BUTTON_ID)
        next_level_button.click()

    def press_up_next_level(self):
        """Press back nabigation next level button."""
        next_level_button = self.driver.find_element_by_id(self.UP_NEXT_LEVEL_BUTTON_ID)
        next_level_button.click()

    def get_counter(self):
        """Returns the current page counter as an int."""
        counter = self.driver.find_element_by_accessibility_id(self.COUNTER_ACCESSIBILITY_ID)
        return int(counter.text)

    def press_back_button(self):
        """Press phone's back button."""
        self.driver.back()
