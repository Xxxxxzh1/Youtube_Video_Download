import os
import xlrd

excel_list = ['video_download.xlsx']
vid_list = []


def getvid_list(name, init_list):
    data = xlrd.open_workbook(f'~/Desktop/{name}')
    sheet_name = data.sheet_names()
    table = data.sheet_by_name(sheet_name[0])
    init_list.extend(table.col_values(2))
    init_list.remove('视频链接')


def downloadvid(name, init_list):
    mkdir_shell = f"mkdir /Volumes/zheng/youtubeVid/{name}"
    os.system(mkdir_shell)
    mv_shell = "mv {} /Volumes/zheng/youtubeTmpVid/{}"
    mvall_shell = f"mv /Volumes/zheng/youtubeTmpVid/* /Volumes/zheng/youtubeVid/{name}/"
    for link in init_list:
        cmd = f"youtube-dl -f 137 -R 'infinite' --exec '{mv_shell}' {link}"
        os.system(cmd)
    os.system(mvall_shell)
    init_list.clear()


if __name__ == "__main__":
    for excel_name in excel_list:
        getvid_list(excel_name, vid_list)
        downloadvid(excel_name, vid_list)
