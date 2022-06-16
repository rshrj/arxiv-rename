import sys
import arxiv

from arxiv_rename.arxiv_rename import arxivRename
from arxiv_rename.arxiv_detect import detect_arxiv


def arxiv_download(download_ids, input_path):
    for download_id in download_ids.split(' '):
        name, isarxiv = detect_arxiv(download_id)
        if not isarxiv:
            return

        print(f'Dowloading {name} to {input_path}')
        paper = list(arxiv.Search(id_list=[download_id]).results())[0]
        written_path = paper.download_pdf(
            dirpath=input_path, filename=f'{download_id}.pdf')
        arxivRename(written_path)


def main():
    arxiv_download(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
