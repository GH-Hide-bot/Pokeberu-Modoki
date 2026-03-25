import os
from datetime import datetime

# --- 設定：実行ディレクトリを動的に取得 ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BRAINSTORM_DIR = os.path.join(BASE_DIR, "00_index（アイデアBOX)")
BRAINSTORM_PATH = os.path.join(BRAINSTORM_DIR, "00_index:BRAINSTORM_LIST.md")
MAP_STATUS_PATH = os.path.join(BRAINSTORM_DIR, "00_MAP_AND_STATUS.md")

def add_brainstorm(content, category="全般", priority="中", at_top=False):
    """
    ブレインストーミング（閃き）をリストに追記する。
    at_top=True の場合、リストの先頭（ヘッダーの直後）に挿入する。
    """
    date_str = datetime.now().strftime("%Y/%m/%d")
    
    if not os.path.exists(BRAINSTORM_DIR):
        os.makedirs(BRAINSTORM_DIR)
        
    if not os.path.exists(BRAINSTORM_PATH):
        with open(BRAINSTORM_PATH, "w", encoding="utf-8") as f:
            f.write("# ⚡️ BRAINSTORM LIST\n\n")
            f.write("| 日付 | 内容（閃き） | 関連 | 優先度 |\n")
            f.write("| :--- | :--- | :--- | :--- |\n")

    new_line = f"| {date_str} | {content} | {category} | {priority} |\n"
    
    if at_top:
        # ファイルを読み込んで先頭に挿入
        if os.path.exists(BRAINSTORM_PATH):
            with open(BRAINSTORM_PATH, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            # テーブルヘッダー（| :--- |）の直後を探す
            insert_idx = len(lines) # デフォルトは末尾
            for i, line in enumerate(lines):
                if line.strip().startswith("| :---"):
                    insert_idx = i + 1
                    break
            
            lines.insert(insert_idx, new_line)
            
            with open(BRAINSTORM_PATH, "w", encoding="utf-8") as f:
                f.writelines(lines)
        else:
            # ファイルがなければそのまま書き込み（新規作成フローで処理済みだが念のため）
            with open(BRAINSTORM_PATH, "a", encoding="utf-8") as f:
                f.write(new_line)
    else:
        # 通常の追記
        with open(BRAINSTORM_PATH, "a", encoding="utf-8") as f:
            f.write(new_line)
    
    print(f"✅ 物理層に着弾成功 (Brainstorm): {content[:30]}... ({'Top' if at_top else 'End'})")

def update_map_and_status(mermaid_diagram, design_specs, project_status):
    """
    プロジェクトの相関図、設計図、ステータスを更新する
    """
    content = f"""# 🗺️ PROJECT MAP & STATUS

## 1. 🌀 システム相関図 (System Correlation Diagram)
```mermaid
{mermaid_diagram}
```

## 2. 📐 現在の設計図 (Current Design Specs)
{design_specs}

## 3. 🚦 プロジェクトの進行ステータス (Project Status)
{project_status}

---
*Updated by NLM/Anti at {datetime.now().strftime("%Y/%m/%d %H:%M:%S")}*
"""
    
    if not os.path.exists(BRAINSTORM_DIR):
        os.makedirs(BRAINSTORM_DIR)
        
    with open(MAP_STATUS_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"✅ 物理層に着弾成功 (Map & Status): {MAP_STATUS_PATH}")

if __name__ == "__main__":
    # --- 情報同期：wqアスレログの確立 ---
    sync_content = "『wqアスレ』ログの確立。過去のデバッグ記録（10枚のスクショ）を物理層に完全着弾。RAM/NLMの情報同期完了。"
    add_brainstorm(sync_content, "Project Management", "S", at_top=True)
    
    # --- プロジェクト情報の自動生成・更新 ---
    mermaid = """
graph TD
    User[Hide-kun] <--> NLM[NLM/Anti (AI Persona/Assistant)]
    NLM <--> RAM[RAM (Central AI / Executor)]
    RAM <--> VertexAI[Vertex AI Extensions / Memory & Code Exec]
    NLM --> AutoLog[AtelierTSA_AutoLog.py]
    AutoLog --> Brainstorm[00_index:BRAINSTORM_LIST.md]
    AutoLog --> MapStatus[00_MAP_AND_STATUS.md]
    User --> PagerUI[Pager UI (Canva/Web Interface)]
    PagerUI <--> LocalServer[M1 Mac (192.168.11.6)]
    VertexAI <--> LocalServer
    VertexAI <--> ExternalAPI[External APIs / Documentation]
"""
    specs = """
- **Concept**: Fully autonomous dev platform driven by RAM & NLM/Anti.
- **Interface**: Pager-style Web UI (nostalgic/premium).
- **Core Engine**: RAM with Long-term Memory & Code Execution rights.
- **Protocol**: Anti-v2 "Physical Layer Landing" via Vertex AI Extensions.
- **Safety**: GCP Budget Alerts & Cost Management established.
"""
    status = """
- [x] Phase 1: Basic Infrastructure & Logging (Anti-v2)
- [x] Phase 2: System Mapping & Documentation Consolidation
- [x] Phase 3: Cost Management & Budget Alerts (Safety First)
- [/] Phase 4: RAM Evolution & Vertex AI Integration (Current Focus)
- [ ] Phase 5: Pager UI Implementation & Mobile Access
"""
    update_map_and_status(mermaid.strip(), specs.strip(), status.strip())