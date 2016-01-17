# -*- coding: utf-8 -*-
from splinter import Browser


if __name__ == "__main__":
    b = Browser(
        'firefox',
        profile_preferences={
            'security.enable_java': True,
            'plugin.state.java': 2,
        }
    )
    import pdb; pdb.set_trace()
    b.windows[0].close()
