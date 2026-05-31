import os
import urllib.request
import time

class PaperDownloader:
    """Classe responsavel por realizar o download de artigos cientificos em PDF do arXiv."""
    
    def __init__(self, target_dir: str):
        self.target_dir = target_dir
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        
    def _ensure_directory_exists(self):
        """Garante que o diretorio de destino existe no sistema."""
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
            print(f"Diretorio criado: {self.target_dir}")
            
    def download_paper(self, filename: str, url: str) -> bool:
        """Realiza o download de um unico artigo e o salva com o nome especificado."""
        dest_path = os.path.join(self.target_dir, filename)
        
        # Verifica se o arquivo ja foi baixado anteriormente
        if os.path.exists(dest_path):
            print(f"Arquivo ja existe, download ignorado: {filename}")
            return True
            
        print(f"Iniciando download de {filename} a partir de {url}...")
        try:
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req) as response:
                with open(dest_path, "wb") as out_file:
                    out_file.write(response.read())
            print(f"Sucesso: {filename} baixado com exito.")
            return True
        except Exception as e:
            print(f"Erro ao baixar {filename}: {str(e)}")
            return False

    def download_all(self, papers_list: list) -> dict:
        """Processa a lista de artigos executando o download em lote."""
        self._ensure_directory_exists()
        results = {}
        
        for filename, url in papers_list:
            success = self.download_paper(filename, url)
            results[filename] = success
            # Delay de seguranca para evitar rate limit do arXiv
            time.sleep(2.0)
            
        return results

if __name__ == "__main__":
    # Definicao do diretorio de destino relativo ao local do paper
    destination_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "related-work-papers")
    
    # Lista de tuplas contendo o nome final do arquivo PDF e a URL direta do arXiv
    papers_to_download = [
        ("Liu2024.pdf", "https://arxiv.org/pdf/2409.02977.pdf"),
        ("Wang2024.pdf", "https://arxiv.org/pdf/2409.09030.pdf"),
        ("Jin2024.pdf", "https://arxiv.org/pdf/2408.02479.pdf"),
        ("Bhati2026.pdf", "https://arxiv.org/pdf/2604.26275.pdf"),
        ("Sengupta2026.pdf", "https://arxiv.org/pdf/2605.25665.pdf"),
        ("Piskala2026.pdf", "https://arxiv.org/pdf/2602.00180.pdf"),
        ("Taghavi2026.pdf", "https://arxiv.org/pdf/2604.05278.pdf"),
        ("Macedo2026.pdf", "https://arxiv.org/pdf/2605.18684.pdf"),
        ("He2025.pdf", "https://arxiv.org/pdf/2404.04834.pdf")
    ]
    
    downloader = PaperDownloader(destination_directory)
    summary = downloader.download_all(papers_to_download)
    
    print("\nResumo do processamento de downloads:")
    for file, status in summary.items():
        result_text = "Sucesso" if status else "Falhou"
        print(f"- {file}: {result_text}")
