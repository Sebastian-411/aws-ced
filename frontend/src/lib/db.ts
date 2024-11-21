import initSqlJs from 'sql.js';

export class ChatDatabase {
  private db: any;
  private static instance: ChatDatabase;
  private initialized: boolean = false;

  private constructor() {}

  static async getInstance() {
    if (!ChatDatabase.instance) {
      ChatDatabase.instance = new ChatDatabase();
      await ChatDatabase.instance.initialize();
    }
    return ChatDatabase.instance;
  }

  private async initialize() {
    if (this.initialized) return;
    
    try {
      const SQL = await initSqlJs({
        locateFile: file => `https://sql.js.org/dist/${file}`
      });
      this.db = new SQL.Database();
      this.createTables();
      this.initialized = true;
    } catch (error) {
      console.error('Failed to initialize database:', error);
      throw new Error('Database initialization failed');
    }
  }

  private createTables() {
    try {
      this.db.run(`
        CREATE TABLE IF NOT EXISTS conversations (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_id TEXT NOT NULL,
          title TEXT NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
      `);

      this.db.run(`
        CREATE TABLE IF NOT EXISTS messages (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          conversation_id INTEGER NOT NULL,
          user_id TEXT NOT NULL,
          content TEXT NOT NULL,
          is_bot BOOLEAN NOT NULL,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
          FOREIGN KEY (conversation_id) REFERENCES conversations(id)
        );
      `);
    } catch (error) {
      console.error('Failed to create tables:', error);
      throw new Error('Table creation failed');
    }
  }

  async createConversation(userId: string, title: string) {
    if (!this.initialized || !this.db) {
      throw new Error('Database not initialized');
    }

    try {
      const result = this.db.exec(
        'INSERT INTO conversations (user_id, title) VALUES (?, ?) RETURNING id',
        [userId, title]
      );
      return result[0].values[0][0];
    } catch (error) {
      console.error('Failed to create conversation:', error);
      throw new Error('Failed to create conversation');
    }
  }

  async saveMessage(conversationId: number, userId: string, content: string, isBot: boolean) {
    if (!this.initialized || !this.db) {
      throw new Error('Database not initialized');
    }

    try {
      this.db.run(
        'INSERT INTO messages (conversation_id, user_id, content, is_bot) VALUES (?, ?, ?, ?)',
        [conversationId, userId, content, isBot]
      );
    } catch (error) {
      console.error('Failed to save message:', error);
      throw new Error('Failed to save message');
    }
  }

  getConversations(userId: string) {
    if (!this.initialized || !this.db) {
      return [];
    }

    try {
      const result = this.db.exec(`
        SELECT id, title, created_at 
        FROM conversations 
        WHERE user_id = ? 
        ORDER BY created_at DESC
      `, [userId]);
      return result[0]?.values || [];
    } catch (error) {
      console.error('Failed to get conversations:', error);
      return [];
    }
  }

  getMessages(conversationId: number) {
    if (!this.initialized || !this.db) {
      return [];
    }

    try {
      const result = this.db.exec(`
        SELECT * FROM messages 
        WHERE conversation_id = ? 
        ORDER BY created_at ASC
      `, [conversationId]);
      return result[0]?.values || [];
    } catch (error) {
      console.error('Failed to get messages:', error);
      return [];
    }
  }
}