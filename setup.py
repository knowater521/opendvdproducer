
from setuptools import setup
import os, sys, subprocess

setup(
    name='Open DVD Producer',
    version=str(open('debian/changelog').read()).split('(')[1].split(')')[0],
    #scripts=['vlc.py'],
    app=['opendvdproducer.py'],
    data_files=[
        ('shared/opendvdproducer/graphics', [   'graphics/add.png',
                                                'graphics/cancel.png',
                                                'graphics/confirm.png',
                                                'graphics/content_panel_background.png',
                                                'graphics/duplicate.png',
                                                'graphics/edit.png',
                                                'graphics/file_not_found.png',
                                                'graphics/finalize_dvd_image.png',
                                                'graphics/finalize_panel_background_button_ddp.png',
                                                'graphics/finalize_panel_background_button_md5.png',
                                                'graphics/finalize_panel_background_button_normal.png',
                                                'graphics/finalize_panel_background_button_over.png',
                                                'graphics/finalize_panel_background_button_toggle_left.png',
                                                'graphics/finalize_panel_background_button_toggle_left_over.png',
                                                'graphics/finalize_panel_background_button_toggle_right.png',
                                                'graphics/finalize_panel_background_button_toggle_right_over.png',
                                                'graphics/finalize_panel_background_left.png',
                                                'graphics/finalize_panel_background_right.png',
                                                'graphics/finalize_panel_options_background.png',
                                                'graphics/import.png',
                                                'graphics/lock_finalize_panel_background.png',
                                                'graphics/menus_properties_panel_background.png',
                                                'graphics/menus_properties_panel_background_center.png',
                                                'graphics/menus_properties_panel_background_file_preview_foreground_4_3.png',
                                                'graphics/menus_properties_panel_background_file_preview_foreground_16_9.png',
                                                'graphics/menus_properties_panel_main_menu_checkbox_checked.png',
                                                'graphics/menus_properties_panel_main_menu_checkbox_unchecked.png',
                                                'graphics/menus_properties_panel_preview_checked.png',
                                                'graphics/menus_properties_panel_preview_unchecked.png',
                                                'graphics/new.png',
                                                'graphics/nowediting_dvd_button_icon.png',
                                                'graphics/nowediting_dvd_button_icon_over.png',
                                                'graphics/nowediting_dvd_panel_aspect_ratio_4_3.png',
                                                'graphics/nowediting_dvd_panel_aspect_ratio_16_9.png',
                                                'graphics/nowediting_dvd_panel_audio_format_ac3.png',
                                                'graphics/nowediting_dvd_panel_audio_format_mp2.png',
                                                'graphics/nowediting_dvd_panel_has_menus_no.png',
                                                'graphics/nowediting_dvd_panel_has_menus_yes.png',
                                                'graphics/nowediting_dvd_panel_video_format_ntsc.png',
                                                'graphics/nowediting_dvd_panel_video_format_pal.png',
                                                'graphics/nowediting_menus_button_icon.png',
                                                'graphics/nowediting_menus_button_icon_over.png',
                                                'graphics/nowediting_panel_background.png',
                                                'graphics/nowediting_panel_background_tab.png',
                                                'graphics/nowediting_videos_button_icon.png',
                                                'graphics/nowediting_videos_button_icon_over.png',
                                                'graphics/open.png',
                                                'graphics/options_panel_background.png',
                                                'graphics/options_panel_dvd_encoding_cbr.png',
                                                'graphics/options_panel_dvd_encoding_vbr.png',
                                                'graphics/options_panel_dvd_image_background.png',
                                                'graphics/options_panel_dvd_layers_dual.png',
                                                'graphics/options_panel_dvd_layers_single.png',
                                                'graphics/options_panel_dvd_passes_one.png',
                                                'graphics/options_panel_dvd_passes_two.png',
                                                'graphics/options_panel_menu_positions.png',
                                                'graphics/preview_4_3_space.png',
                                                'graphics/preview_16_9_space.png',
                                                'graphics/remove.png',
                                                'graphics/save.png',
                                                'graphics/top_panel_background.png',
                                                'graphics/videos_player_controls_panel_background.png',
                                                'graphics/videos_player_controls_panel_frameback_background.png',
                                                'graphics/videos_player_controls_panel_frameback_over.png',
                                                'graphics/videos_player_controls_panel_frameback_press.png',
                                                'graphics/videos_player_controls_panel_frameforward_background.png',
                                                'graphics/videos_player_controls_panel_frameforward_over.png',
                                                'graphics/videos_player_controls_panel_frameforward_press.png',
                                                'graphics/videos_player_controls_panel_mark_background.png',
                                                'graphics/videos_player_controls_panel_mark_over.png',
                                                'graphics/videos_player_controls_panel_mark_press.png',
                                                'graphics/videos_player_controls_panel_pause_background.png',
                                                'graphics/videos_player_controls_panel_pause_over.png',
                                                'graphics/videos_player_controls_panel_pause_press.png',
                                                'graphics/videos_player_controls_panel_play_background.png',
                                                'graphics/videos_player_controls_panel_play_over.png',
                                                'graphics/videos_player_controls_panel_play_press.png',
                                                'graphics/videos_player_controls_panel_stop_background.png',
                                                'graphics/videos_player_controls_panel_stop_over.png',
                                                'graphics/videos_player_controls_panel_stop_press.png',
                                                'graphics/videos_player_controls_panel_trimend_background.png',
                                                'graphics/videos_player_controls_panel_trimend_over.png',
                                                'graphics/videos_player_controls_panel_trimend_press.png',
                                                'graphics/videos_player_controls_panel_trimstart_background.png',
                                                'graphics/videos_player_controls_panel_trimstart_over.png',
                                                'graphics/videos_player_controls_panel_trimstart_press.png',
                                                'graphics/videos_player_timeline_background.png',
                                                'graphics/videos_player_timeline_end.png',
                                                'graphics/videos_player_timeline_seek.png',
                                                'graphics/videos_player_timeline_start.png'
                                            ]),
        ('shared/opendvdproducer/graphics', ['graphics/file_not_found.mkv']),
        ('shared/opendvdproducer/resources', [  'resources/Ubuntu-B.ttf',
                                                'resources/Ubuntu-BI.ttf',
                                                'resources/UbuntuMono-R.ttf',
                                                'resources/Ubuntu-R.ttf',
                                                'resources/Ubuntu-RI.ttf'
                                             ]),
        ('shared/opendvdproducer/resources', ['resources/silence.flac']),
        ('share/opendvdproducer', ['opendvdproducer.py']),
        ('share/opendvdproducer', ['vlc.py']),
        ('bin', ['bin/opendvdproducer']),
        ('share/applications', ['bin/opendvdproducer.desktop']),
        ('share/pixmaps', ['pixmaps/opendvdproducer.png'])
    ],
    options={},
    setup_requires=[],
)
