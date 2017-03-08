class ShamElement:
    def __init__(self, element):
        """
        :param element: xml.etree.ElementTree.Element
        """
        self._element = element

        bounds_str = self._element.get('bounds')

        bounds = bounds_str.split(',')
        x_left = int(bounds[0].strip('['))
        y_up = int(bounds[1].split(']')[0])
        x_right = int(bounds[1].split(']')[1].strip('['))
        y_down = int(bounds[2].strip(']'))

        x = x_left
        y = y_up
        width = x_right - x_left
        height = y_down - y_up

        self.rect = {'x': x, 'y': y, 'width': width, 'height': height}
