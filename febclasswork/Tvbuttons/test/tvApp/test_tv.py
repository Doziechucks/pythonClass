from unittest import TestCase

from source.TvApp.tv_buttons import Television


class TestTvInterface(TestCase):
    def setUp(self):
        self.my_tv = Television()

    def test_the_tv_current_state(self):
        self.assertFalse(self.my_tv.status())

    def test_if_tv_comes_on(self):
        self.my_tv.turn_on()
        expected = self.my_tv.status()
        self.assertEqual(True, expected)

    def test_if_tv_goes_off(self):
        self.my_tv.turn_on()
        self.my_tv.turn_off()
        expected = self.my_tv.status()
        self.assertEqual(False, expected)

    def test_if_volume_increases(self):
        self.my_tv.turn_on()
        self.my_tv.volume_up(1)
        actual = self.my_tv.current_volume()
        expected = 1
        self.assertEqual(expected, actual)

    def test_if_volume_is_zero_off(self):
        self.my_tv.volume_up(1)
        actual = self.my_tv.current_volume()
        expected = 0
        self.assertEqual(actual, expected)

    def test_if_volume_down_works_properly(self):
        self.my_tv.volume_down(1)
        actual = self.my_tv.current_volume()
        expected = 0
        self.assertEqual(actual, expected)

    def test_if_volume_down_works(self):
        self.my_tv.turn_on()
        self.my_tv.volume_up(3)
        self.my_tv.volume_up(1)
        self.my_tv.volume_down(2)
        actual = self.my_tv.current_volume()
        expected = 2
        self.assertEqual(actual, expected)

    def test_if_channel_and_up_down_works(self):
        self.my_tv.turn_on()
        self.my_tv.channel_up(3)
        self.my_tv.channel_up(1)
        self.my_tv.channel_down(3)
        actual = self.my_tv.current_channel()
        expected = 2
        self.assertEqual(actual, expected)

    def test_if_mute_works(self):
        self.my_tv.turn_on()
        self.my_tv.volume_up(25)
        self.my_tv.mute()
        actual = self.my_tv.current_volume()
        expected = 0
        self.assertEqual(actual, expected)

    def test_if_mute_unmute_works(self):
        self.my_tv.turn_on()
        self.my_tv.volume_up(25)
        self.my_tv.mute()
        self.my_tv.unmute()
        actual = self.my_tv.current_volume()
        expected = 25
        self.assertEqual(actual, expected)






