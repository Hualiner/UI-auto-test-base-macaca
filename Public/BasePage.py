from macaca import WebDriverException


class BasePage(object):
    @classmethod
    def set_driver(cls, dri):
        cls.driver = dri

    def get_driver(self):
        return self.driver

    def _get_window_size(self):
        window = self.driver.get_window_size()
        y = window['height']
        x = window['width']

        return x, y

    @staticmethod
    def _get_element_size(element):
        rect = element.rect

        x_center = rect['x'] + rect['width'] / 2
        y_center = rect['y'] + rect['height'] / 2
        x_left = rect['x']
        y_up = rect['y']
        x_right = rect['x'] + rect['width']
        y_down = rect['y'] + rect['height']

        return x_left, y_up, x_center, y_center, x_right, y_down

    def _swipe(self, fromX, fromY, toX, toY, steps):
        self.driver \
            .touch('drag', {'fromX': fromX, 'fromY': fromY, 'toX': toX, 'toY': toY, 'steps': steps})

    def swipe_up(self, element=None, steps=10):
        """
        swipe up
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_up
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.5*x
            toY = 0.25*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_down(self, element=None, steps=10):
        """
        swipe down
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_center
            toY = y_down
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.5*x
            toY = 0.75*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_left(self, element=None, steps=10):
        """
        swipe left
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_left
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.25*x
            toY = 0.5*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def swipe_right(self, element=None, steps=10):
        """
        swipe right
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :return: None
        """
        if element:
            x_left, y_up, x_center, y_center, x_right, y_down = self._get_element_size(element)

            fromX = x_center
            fromY = y_center
            toX = x_right
            toY = y_center
        else:
            x, y = self._get_window_size()
            fromX = 0.5*x
            fromY = 0.5*y
            toX = 0.75*x
            toY = 0.5*y

        self._swipe(fromX, fromY, toX, toY, steps)

    def _find_element_by_swipe(self, direction, using, value, element=None, steps=10, max_swipe=5):
        times = max_swipe

        for i in range(times):
            try:
                return self.driver.element(using, value)
            except WebDriverException:
                if direction == 'up':
                    self.swipe_up(element=element, steps=steps)
                elif direction == 'down':
                    self.swipe_down(element=element, steps=steps)
                elif direction == 'left':
                    self.swipe_left(element=element, steps=steps)
                elif direction == 'right':
                    self.swipe_right(element=element, steps=steps)

                if i == times - 1:
                    raise WebDriverException

    def find_element_by_swipe_up(self, using, value, element=None, steps=10, max_swipe=5):
        """
        find element by swipe up
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('up', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_down(self, using, value, element=None, steps=10, max_swipe=5):
        """
        find element by swipe down
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('down', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_left(self, using, value, element=None, steps=10, max_swipe=5):
        """
        find element by swipe left
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('left', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_by_swipe_right(self, using, value, element=None, steps=10, max_swipe=5):
        """
        find element by swipe right
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        return self._find_element_by_swipe('right', using, value,
                                           element=element, steps=steps, max_swipe=max_swipe)

    def find_element_on_horizontal(self, using, value, element=None, steps=10, max_swipe=5):
        """
        find element on horizontal
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        try:
            return self.find_element_by_swipe_left(using, value,
                                                   element=element, steps=steps, max_swipe=max_swipe)
        except WebDriverException:
            pass

        return self.find_element_by_swipe_right(using, value,
                                                element=element, steps=steps, max_swipe=max_swipe)

    def find_element_on_vertical(self, using, value, element=None, steps=10, max_swipe=5):
        """
        find element on vertical
        :param using: The element location strategy.
                      "id","xpath","link text","partial link text","name","tag name","class name","css selector"
        :param value: The value of the location strategy.
        :param element: WebElement of Macaca, if None while swipe window of phone
        :param steps: steps of swipe for Android, The lower the faster
        :param max_swipe: the max times of swipe
        :return: WebElement of Macaca

        Raises:
            WebDriverException.
        """
        try:
            return self.find_element_by_swipe_up(using, value,
                                                 element=element, steps=steps, max_swipe=max_swipe)
        except WebDriverException:
            pass

        return self.find_element_by_swipe_down(using, value,
                                               element=element, steps=steps, max_swipe=max_swipe)

    def _tap(self, x, y):
        self.driver.touch('tap', {'x': x, 'y': y})

    def _click_side_of_element(self, direction, element, rate):
        rect = element.rect

        width = rect['width']
        height = rect['height']

        x_center = rect['x'] + rect['width'] / 2
        y_center = rect['y'] + rect['height'] / 2

        x_left = rect['x']
        y_up = rect['y']
        x_right = rect['x'] + rect['width']
        y_down = rect['y'] + rect['height']

        x = y = 0
        if direction == 'above':
            x = x_center
            y = y_up - rate * height
        elif direction == 'under':
            x = x_center
            y = y_down + rate * height
        elif direction == 'left':
            x = x_left - rate * width
            y = y_center
        elif direction == 'right':
            x = x_right + rate * width
            y = y_center

        self._tap(x, y)

    def click_above_of_element(self, element, rate=1):
        """
        click above the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('above', element, rate)

    def click_under_of_element(self, element, rate=1):
        """
        click under the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('under', element, rate)

    def click_left_of_element(self, element, rate=1):
        """
        click the left of the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('left', element, rate)

    def click_right_of_element(self, element, rate=1):
        """
        click the right of the gaven element
        :param element: WebElement of Macaca
        :param rate: rate of the width or height of the element
        :return: None
        """
        self._click_side_of_element('right', element, rate)
