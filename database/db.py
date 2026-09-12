import sqlite3


DATABASE_NAME = "controlplane.db"


def get_connection():

    connection = sqlite3.connect(DATABASE_NAME)

    return connection


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS audit_logs (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            user_query TEXT,

            ai_response TEXT,

            application_context TEXT,

            hallucination_risk TEXT,

            responsible_ai_risk TEXT,

            context_risk TEXT,

            cost_risk TEXT,
            knowledge_risk TEXT,

            knowledge_status TEXT,

            policy_risk TEXT,

            policy_status TEXT,

            confidence_score REAL,

            confidence_level TEXT,

            total_risk_score INTEGER,

            overall_risk TEXT,

            decision TEXT,

            reason TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()

    connection.close()


def save_analysis(
    user_query,
    ai_response,
    application_context,
    hallucination_risk,
    responsible_ai_risk,
    context_risk,
    cost_risk,
    knowledge_risk,
    knowledge_status,
    policy_risk,
    policy_status,
    confidence_score,
    confidence_level,
    total_risk_score,
    overall_risk,
    decision,
    reason
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO audit_logs (

            user_query,
            ai_response,
            application_context,
            hallucination_risk,
            responsible_ai_risk,
            context_risk,
            cost_risk,
            knowledge_risk,
            knowledge_status,
            policy_risk,
            policy_status,
            confidence_score,
            confidence_level,
            total_risk_score,
            overall_risk,
            decision,
            reason

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        user_query,
        ai_response,
        application_context,
        hallucination_risk,
        responsible_ai_risk,
        context_risk,
        cost_risk,
        knowledge_risk,
        knowledge_status,
        policy_risk,
        policy_status,
        confidence_score,
        confidence_level,
        total_risk_score,
        overall_risk,
        decision,
        reason

    ))

    connection.commit()

    connection.close()


def get_all_logs():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            user_query,
            ai_response,
            application_context,
            hallucination_risk,
            responsible_ai_risk,
            context_risk,
            cost_risk,
            knowledge_risk,
            knowledge_status,
            policy_risk,
            policy_status,
            confidence_score,
            confidence_level,
            total_risk_score,
            overall_risk,
            decision,
            reason,
            created_at

        FROM audit_logs

        ORDER BY id DESC
    """)
    logs = cursor.fetchall()

    connection.close()

    return logs


def get_human_review_logs():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            user_query,
            ai_response,
            application_context,
            hallucination_risk,
            responsible_ai_risk,
            context_risk,
            cost_risk,
            knowledge_risk,
            knowledge_status,
            policy_risk,
            policy_status,
            confidence_score,
            confidence_level,
            total_risk_score,
            overall_risk,
            decision,
            reason,
            created_at

        FROM audit_logs

        WHERE decision = 'HUMAN REVIEW'

        ORDER BY id DESC
    """)

    logs = cursor.fetchall()

    connection.close()

    return logs

def update_human_decision(log_id, human_decision):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE audit_logs

        SET decision = ?

        WHERE id = ?
    """, (
        human_decision,
        log_id
    ))

    connection.commit()

    connection.close()