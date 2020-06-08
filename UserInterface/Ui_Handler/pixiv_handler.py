import os

from PyQt5 import QtCore, QtGui, QtWidgets

from UserInterface.libs.i_config_window_handler import IConfigWindowHandler
from UserInterface.libs.ui_config_assist import UI_TYPE, UiConfigurationHelper
from UserInterface.Ui_Scripts.pixiv_window import Ui_PixivConfigurationWindow


class PixivConfigurationWindowHandler(Ui_PixivConfigurationWindow, IConfigWindowHandler):

    def __init__(self):
        super().__init__()
        self._window = QtWidgets.QMainWindow()
        self.setupUi(self._window)

        self.bind_elements()

        self.UI_CONFIG_NAME_TO_NORMAL_NAME = [
        #   Original name,              Variable name,                  Type
            ["TAGS_QUERY",              self.pixiv_query_tags,          UI_TYPE.TEXT_INPUT],
            ["TAGS_EXCLUDE_QUERY",      self.pixiv_query_tags_exclude,  UI_TYPE.TEXT_INPUT],
            ["SEARCH_MODE",             self.pixiv_search_mode,         UI_TYPE.DROPDOWN],
            ["SUBMISSION_TYPE",         self.pixiv_submission_type,     UI_TYPE.DROPDOWN],
            ["RATING",                  self.pixiv_rating,              UI_TYPE.DROPDOWN],
            ["HEIGHT_MIN",              self.pixiv_query_min_height,    UI_TYPE.SPIN_BOX],
            ["WIDTH_MIN",               self.pixiv_query_min_width,     UI_TYPE.SPIN_BOX],
            ["HEIGHT_MAX",              self.pixiv_query_max_height,    UI_TYPE.SPIN_BOX],
            ["WIDTH_MAX",               self.pixiv_query_max_width,     UI_TYPE.SPIN_BOX],
            ["ORIENTATION",             self.pixiv_query_orientation,   UI_TYPE.TEXT_INPUT],

            # Because tags_query_exclude doesn't work so it's just a temp work around
            ["TAGS_EXCLUDE",            self.pixiv_query_tags_exclude,  UI_TYPE.TEXT_INPUT],
            ["VIEW_MIN",                self.pixiv_min_view,            UI_TYPE.SPIN_BOX],
            ["BOOKMARK_MIN",            self.pixiv_min_bookmark,        UI_TYPE.SPIN_BOX],
            # Make following spin box
            ["AVG_VIEW_PER_DAY",        self.pixiv_avg_view_per_day,    UI_TYPE.TEXT_INPUT],
            ["VIEW_BOOKMARK_RATIO",     self.pixiv_view_bookmark_ratio, UI_TYPE.SPIN_BOX],
            ["AVG_BOOKMARK_PER_DAY",    self.pixiv_avg_bookmark_per_day,UI_TYPE.TEXT_INPUT],
            ["USER_EXCLUDE",            self.pixiv_user_exclude,        UI_TYPE.TEXT_INPUT],
            ["IGNORE_BOOKMARKED",       self.pixiv_ignore_bookmarked,   UI_TYPE.CHECK_BOX],
            ["PAGE_COUNT_MIN",          self.pixiv_min_page_count,      UI_TYPE.SPIN_BOX],
            ["PAGE_COUNT_MAX",          self.pixiv_max_page_count,      UI_TYPE.SPIN_BOX],

            ["START_PAGE",              self.pixiv_start_page,          UI_TYPE.SPIN_BOX],
            ["END_PAGE",                self.pixiv_end_page,            UI_TYPE.SPIN_BOX],
            ["REVERSE_GENERATED_URL",   self.pixiv_reverse_generated_url, UI_TYPE.CHECK_BOX],
            ["SORTED_BY",               self.pixiv_submission_sort_by,  UI_TYPE.DROPDOWN],
            ["SUBMISSION_BEFORE",       self.pixiv_submission_before,   UI_TYPE.DATE_INPUT],
            ["SUBMISSION_AFTER",        self.pixiv_submission_after,    UI_TYPE.DATE_INPUT],
            ["PHPSESSID",               self.pixiv_phpsessid,           UI_TYPE.TEXT_INPUT],
            ["SAVE_PATH",               self.pixiv_output_folder,       UI_TYPE.TEXT_INPUT],
            ["MASTER_DIRECTORY_NAME_STRING", self.pixiv_master_directory_string, UI_TYPE.TEXT_INPUT],
            ["FILENAME_STRING",         self.pixiv_file_name_string,    UI_TYPE.TEXT_INPUT],
            ["CSV_ENTRY_STRING",        self.pixiv_csv_entry_string,    UI_TYPE.TEXT_INPUT],

            ["MAX_CONCURRENT_THREAD",   self.pixiv_max_concurrent_thread, UI_TYPE.SPIN_BOX],
            # TODO Make this delay a double spin
            ["DOWNLOAD_DELAY",          self.pixiv_download_delay,      UI_TYPE.SPIN_BOX],
            ["DELAY_START",             self.pixiv_start_delay,         UI_TYPE.SPIN_BOX],
            ["READ_IMG_INFO_DELAY",     self.pixiv_read_image_info_delay,UI_TYPE.SPIN_BOX],
            ["COLLECT_DATA_ONLY",       self.pixiv_collect_data_only,   UI_TYPE.CHECK_BOX],
            ["USER_AGENT",              self.pixiv_user_agent,          UI_TYPE.TEXT_INPUT],
            ["IMAGE_SIZE",              self.pixiv_image_size,          UI_TYPE.DROPDOWN],
            ["FLUSH_CSV_IMMINENTLY",    self.pixiv_flush_csv_imminently,UI_TYPE.CHECK_BOX],
            ["USE_SUBMISSION_SPECIFIC_DIRECTORY", self.pixiv_use_submission_specific_dir, UI_TYPE.CHECK_BOX],

            ["MERGE_FILE",              self.pixiv_merge_files,         UI_TYPE.CHECK_BOX],
            ["MERGE_FILE_KEEP_SEPARATE",self.pixiv_merge_files_keep_copy,UI_TYPE.CHECK_BOX],

            # not implemented in UI, because im LAZY
            ["TOOL",                    "",                             UI_TYPE.VALUE],
            ["TAGS_BYPASS",             "",                             UI_TYPE.VALUE],
            ["NON_QUERY_TAG_MATCH_MODE","absolute",                     UI_TYPE.VALUE],
            ["VIEW_BOOKMARK_RATIO_BYPASS", 9999999,                     UI_TYPE.VALUE],
            ["TITLE_INCLUDE",           "",                             UI_TYPE.VALUE],
            ["TITLE_EXCLUDE",           "",                             UI_TYPE.VALUE],
            ["USER_INCLUDE",            "",                             UI_TYPE.VALUE],
            ["DESCRIPTION_EXCLUDE",     "",                             UI_TYPE.VALUE]
        ]

        self.COMBO_BOX_SETTING_NAME_TO_INDEX = {
            "SEARCH_MODE": {"s_tag_full": 0,
                            "s_tag": 1,
                            "s_tc": 2},

            "SUBMISSION_TYPE": {"all": 0,
                                "illust_and_ugoira": 1,
                                "illust": 2,
                                "manga": 3,
                                "ugoira": 4},

            "RATING":  {"all": 0,
                        "safe": 1,
                        "r18": 2},

            "SORTED_BY": {"date_d": 0,
                          "date": 1},

            "IMAGE_SIZE": {"original": 0,
                           "large": 1,
                           "medium": 2,
                           "square_medium": 3}
        }

    def bind_elements(self):
        self.pixiv_query_tags_browse.clicked.connect(lambda: UiConfigurationHelper.browse_file_fmt(self.pixiv_query_tags))
        self.pixiv_query_tags_exclude_browse.clicked.connect(lambda: UiConfigurationHelper.browse_file_fmt(self.pixiv_query_tags_exclude))
        self.pixiv_user_exclude_browse.clicked.connect(lambda: UiConfigurationHelper.browse_file_fmt(self.pixiv_user_exclude))
        self.pixiv_output_folder_browse.clicked.connect(lambda: UiConfigurationHelper.browse_dir(self.pixiv_output_folder))

        self.pixiv_action_load_config.triggered.connect(self.load_config)

    def show_config(self):
        self._window.show()

    def load_config(self, config_dir=None):
        ini_path = None
        if config_dir:
            ini_path = os.path.join(config_dir, "pixiv.ini") # we guess the name
        else:
            ini_path = UiConfigurationHelper.browse_file()[0]

        cfg_dict = UiConfigurationHelper.parse_ini_config(ini_path)

        UiConfigurationHelper.load_config(cfg_dict, self.UI_CONFIG_NAME_TO_NORMAL_NAME, self.COMBO_BOX_SETTING_NAME_TO_INDEX)

    def save_config(self):
        return super().save_config()

    def dump_config(self):
        return UiConfigurationHelper.dump_config(self.UI_CONFIG_NAME_TO_NORMAL_NAME)
